import { ReactElement } from 'react'
import ProfileLayout from './layout'
import styles from '../catalog/Catalog.module.scss'
import Assets from '../../components/Assets/Assets'
import dynamic from 'next/dynamic'
import { GetServerSideProps } from 'next'
import nookies from 'nookies'

const DynamicFilter = dynamic(() => import('../../components/Filter/FilterBlock'), {
  ssr: false
})

const Purchased = () => {
  return (
    <div className={styles.container}>
      <DynamicFilter/>
      <Assets />
    </div>
  )
}

Purchased.getLayout = function getLayout(page: ReactElement) {
  return (
    <ProfileLayout>
      {page}
    </ProfileLayout>
  )
}

export const getServerSideProps: GetServerSideProps = async (context) => {

  const cookies = nookies.get(context)

  const accessToken = cookies['accessToken']

  if (accessToken) {
    const response = await fetch('http://localhost:5000/users', {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`
      },
      method: 'GET'
    })

    if (!response.ok) {
      console.log(response.statusText)
      return {
        props: {
          data: [],
          message: 'Internal server error'
        }
      }
    }

    const data = await response.json()

    return {
      props: {
        data,
        message: 'success'
      }
    }
  } else {
    return {
      redirect: {
        destination: '/auth',
        permanent: false
      }
    }
  }
}

export default Purchased