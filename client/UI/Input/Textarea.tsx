import { forwardRef, InputHTMLAttributes, TextareaHTMLAttributes } from 'react'
import styles from './Textarea.module.scss'

/**
 * Компонент ввода текста
 */

const Textarea = forwardRef<HTMLTextAreaElement, TextareaHTMLAttributes<HTMLTextAreaElement>>(function Textarea(
  { className, ...rest },
  ref,
) {
  return (
    <textarea
      ref={ref}
      className={[styles.base, className].join(' ')}
      autoComplete="off"
      {...rest}
    />
  )
})

export default Textarea
